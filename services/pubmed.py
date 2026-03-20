import os

from Bio import Entrez

Entrez.email = os.getenv("PUBMED_EMAIL")


def fetch_pubmed_context(symptoms: str, max_results: int = 3):
    """
    Fetch relevant article titles from PubMed based on symptoms
    """

    try:
        search = Entrez.esearch(
            db="pubmed",
            term=symptoms,
            retmax=max_results
        )
        record = Entrez.read(search)
        ids = record["IdList"]

        if not ids:
            return "No relevant medical literature found."

        fetch = Entrez.efetch(
            db="pubmed",
            id=",".join(ids),
            rettype="abstract",
            retmode="text"
        )

        articles = fetch.read()

        return articles[:2000]  # limit context size

    except Exception as e:
        return f"Error fetching PubMed data: {str(e)}"