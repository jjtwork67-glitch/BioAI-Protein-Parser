import os
import requests
from Bio import SeqIO

def fetch_and_read_protein():
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id=AAA59172.1&rettype=fasta"
    filename = "insulin.fasta"
    
    if not os.path.exists(filename):
        print("Downloading Human Insulin FASTA file from NCBI...")
        response = requests.get(url)
        with open(filename, "w") as file:
            file.write(response.text)
        print("Download complete!\n")

    print("--- Biopython Protein Analysis ---")
    with open(filename, "r") as file:
        protein_record = SeqIO.read(file, "fasta")
        
        protein_id = protein_record.id
        protein_sequence = protein_record.seq
        protein_description = protein_record.description
        
        print(f"Database ID: {protein_id}")
        print(f"Description: {protein_description}")
        print(f"Protein Length: {len(protein_sequence)} amino acids")
        print(f"Raw Sequence String:\n{protein_sequence}")

if __name__ == "__main__":
    fetch_and_read_protein()