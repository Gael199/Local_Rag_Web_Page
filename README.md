# Chat avec une page web — RAG local 🌐

Ce projet est une application **RAG** (*Retrieval-Augmented Generation*) locale qui permet de discuter avec le contenu d’une page web.

L’utilisateur entre l’URL d’une page web, l’application récupère son contenu, le découpe en morceaux, crée des embeddings, stocke ces informations dans une base vectorielle locale, puis permet de poser des questions sur cette page.

L’application utilise **Streamlit**, **LangChain**, **ChromaDB** et **Ollama** avec des modèles locaux.

---

## Fonctionnalités

- Charger le contenu d’une page web à partir d’une URL
- Découper automatiquement le texte en petits morceaux
- Créer des embeddings localement avec Ollama
- Stocker les documents dans une base vectorielle ChromaDB
- Retrouver les passages les plus pertinents selon la question
- Générer une réponse avec un modèle local
- Fonctionner en local via une interface Streamlit

---

## Technologies utilisées

- Python
- Streamlit
- LangChain
- ChromaDB
- Ollama
- TinyLlama
- nomic-embed-text

---

## Structure du projet

```text
.
├── local_rag_eudes.py
├── requirements.txt
├── README.md
└── .gitignore
