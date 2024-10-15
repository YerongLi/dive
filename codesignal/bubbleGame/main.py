def eliminate_bubbles(bubble, operations):
    n, m = len(bubble), len(bubble[0])  # n rows, m cols

    def drop_bubbles():
        for col in range(m):
            empty_rows = [row for row in range(n) if bubble[row][col] == 0]
            filled_rows = [row for row in range(n) if bubble[row][col] != 0]
            for i, row in enumerate(empty_rows + filled_rows):
                if i < len(empty_rows):
                    bubble[row][col] = 0
                else:
                    bubble[row][col] = bubble[filled_rows[i-len(empty_rows)]][col]

    def check_and_eliminate(r, c):
        if bubble[r][c] == 0:
            return False  # Do nothing for empty cell

        value = bubble[r][c]
        to_eliminate = {(r, c)}
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and bubble[nr][nc] == value:
                to_eliminate.add((nr, nc))

        if len(to_eliminate) > 2:
            for er, ec in to_eliminate:
                bubble[er][ec] = 0
            return True
        return False

    for r, c in operations:
        if check_and_eliminate(r, c):
            drop_bubbles()

    return bubble

# Example
bubble = [
    [1, 2, 3],
    [1, 2, 4],
    [1, 2, 2]
]

operations = [
    [0, 1],
    [2, 1]
]

print(eliminate_bubbles(bubble, operations))

    def _post_encode(self, model, data: Any) -> Dict[str, Any]:
        res = super()._post_encode(model, data)
        temp_len = res['inputs_embeds'].shape[0]
        if  temp_len> self.query_max_len:
            raise MaxLengthExceededError(
                f"Input length {res['inputs_embeds'].shape[0]} exceeds the maximum allowed length of {query_max_len}."
            )
        # Get the input embeddings for the padding token, assume pad shape is [1]
        pad_emb = model.get_input_embeddings()(torch.tensor([self.tokenizer.pad_token_id]).to(model.device)) # Shape: [1, 4096]
        # Extract current embeddings and im_mask
        inputs_embeds = res['inputs_embeds']         # Shape: [current_len, 4096]
        im_mask = res['im_mask']                     # Shape: [current_len]
        # res.pop('inputs_embeds')
        res_len = self.query_max_len - temp_len
        
        # Expand eos_embedding to the required padding length
        pad_emb = pad_emb.expand(res_len, -1).to(model.device)  # Shape: [res_len, 4096]

        # Right-pad the inputs_embeds by concatenating eos embeddings
        padded_inputs_embeds = torch.cat([inputs_embeds, pad_emb], dim=0)  # Shape: [query_max_len, 4096]

        # Create padded attention_mask (extend with zeros)
        attention_mask = torch.cat([torch.ones(1, temp_len), torch.zeros(1, res_len)], dim=1).to(model.device)  # Shape: [query_max_len]
        # Right-pad the im_mask with zeros to match the new length
        padded_im_mask = torch.cat([im_mask, torch.zeros((1, res_len), dtype=torch.bool).to(model.device)], dim=1)  # Shape: [1, query_max_len]
        padded_target =res['labels'] + [-100] * res_len  # Shape: [1, query_max_len]
        
        # Update the res dictionary
        res['inputs_embeds'] = padded_inputs_embeds
        res['attention_mask'] = attention_mask
        res['im_mask'] = padded_im_mask
        res['labels'] = padded_target
        return res