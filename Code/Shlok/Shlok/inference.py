def summarize_violation(text, model, tokenizer, max_length=128):
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    outputs = model.generate(**inputs, max_new_tokens=max_length)
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return summary