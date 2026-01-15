# RLM推論ノート（Recursive Language Models）

## 位置づけ
- RLMは推論時スケーリングの戦略で、長文プロンプトをモデル外部の環境（REPL変数）として扱う。
- LLMはコードで「探索・分割・再帰呼び出し」を行い、必要箇所だけを処理する。

## コア原理
- 長文を直接モデルに流し込まず、外部環境のオブジェクトとして扱う。
- 再帰サブコールを許し、サブタスクを階層的に解く。
- 段階的ロードと相性が良い（必要な部分だけ読む）。

## 評価タスク（論文）
- S-NIAH（needle-in-a-haystackの単一針タスク）。
- BrowseComp-Plus（多数文書のマルチホップQA）。
- OOLONG（入力のほぼ全行を使う線形複雑度タスク）。
- OOLONG-Pairs（入力ペア集約の二次複雑度タスク）。
- LongBench-v2 CodeQA（コードリポ理解）。

## 比較対象（ベースライン）
- ベースLLMの直接回答。
- 要約/コンパクション系の反復エージェント。
- CodeAct（ReAct系）+ BM25 などのリトリーバ併用。
- RLMのアブレーション（REPLは使うが再帰サブコールなし）。

## 主な結果（要点）
- 有効入力長がモデル文脈の2桁上まで拡張可能と報告。
- 10M+トークン規模でも強い性能を示し、長文処理で他手法を大きく上回る。
- コストは同等か、場合によってはより低い。

## 実装の要点（REPL型RLM）
- REPLに長文を変数として置き、探索・分割・集約をコードで行う。
- サブLM呼び出しは高コストのため、バッチ化・回数制御が重要。

## ネガティブ結果 / 限界
- 同一プロンプトを全モデルに使うと挙動が不安定になり得る（モデル別調整が必要）。
- コーディング能力が弱いモデルはRLMとして機能しにくい。
- 出力トークン上限が低い「思考モデル」は、長い推論で失敗しやすい。
- サブコールを同期的に行うと遅くなる（非同期化が望ましい）。
- FINALタグによる終了判定は脆く、誤って思考を最終回答として出すことがある。

## 設計に落とすための示唆
- 「検索→抽出→検証→統合」の再帰タスクに分ける。
- agentsは仕様のみ、知識はreferencesへ。
- scriptsで機械処理（抽出・整形・差分）を外出しする。
- RLM運用は「サブコール回数」「出力トークン上限」「非同期実行」を前提に設計する。

## 公式情報
- 公式コードベースは作者ブログから案内されている。
- 最小実装（rlm-minimal）も公開されている。

## 関連論文/記事（URL）
| 論文/記事名 | URL | 備考 |
| --- | --- | --- |
| **Recursive Language Models** | https://arxiv.org/abs/2512.24601 | スレ主張のRLM（MIT側論文）。 |
| **RLM PDF** | https://arxiv.org/pdf/2512.24601 | 同上のPDF版。 |
| **RETRO Blog** | https://deepmind.google/blog/improving-language-models-by-retrieving-from-trillions-of-tokens/ | DeepMindの検索拡張モデル。 |
| **RAG（arXiv）** | https://arxiv.org/abs/2005.11401 | RAGの元論文。 |
| **Recursive Transformer (DeepMind)** | https://deepmind.google/research/publications/122290/ | 別系研究。 |
