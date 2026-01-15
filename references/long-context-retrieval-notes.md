# Long-Context + Retrieval Notes (RLM / RAG / RETRO / Recursive Transformer)

## RLM (Recursive Language Models)
- Long prompts are treated as an **external environment**; the LM **programmatically inspects** and **recursively calls itself** over snippets.
- Handles contexts **orders of magnitude beyond** model limits; performs strongly on long-context tasks.
- Benchmarks include **S-NIAH**, **BrowseComp-Plus**, **OOLONG**, **OOLONG-Pairs**, **LongBench-v2 CodeQA**.
- Information-dense tasks (OOLONG / OOLONG-Pairs) **require recursive sub-calls**.

## RAG (Retrieval-Augmented Generation)
- Combines **parametric memory** (seq2seq LM) with **non-parametric memory** (retrieved documents).
- Uses **DPR** retriever over a dense index (e.g., Wikipedia) and a generator (e.g., BART).
- **RAG-Sequence**: one latent document for the whole output sequence.
- **RAG-Token**: document can vary per token; allows mixing evidence across docs.
- Non-parametric memory can be **replaced to update knowledge**.

## RETRO (Retrieval-Enhanced Transformer)
- Augments transformers with retrieval over a **very large corpus** (trillions of tokens).
- Nearest-neighbor retrieval provides passages + continuations; cross-attention integrates them.
- Improves factuality and performance relative to comparable-size dense LMs.

## Recursive Transformer (parameter sharing)
- Shares parameters across layers by **looping a single block**.
- Uses **layer-wise LoRA** to specialize per loop with minimal overhead.
- Enables **continuous depth-wise batching** and throughput gains with dynamic depth.

## Design Implications for Skills
- Prefer **search → extract → verify → synthesize** over full-context reads.
- Classify tasks by input complexity (constant / linear / quadratic) and choose RLM patterns accordingly.
- Use retrieval + small summaries instead of long raw contexts.
