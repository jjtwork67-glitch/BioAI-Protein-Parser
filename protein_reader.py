import os
import requests
from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis  # New analytics tool!

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
        print(f"Raw Sequence String:\n{protein_sequence}\n")
        
        # --- NEW BIOCHEMICAL ANALYTICS SECTION ---
        print("--- Calculating Biochemical Properties ---")
        
        # We pass the text sequence into the ProteinAnalysis machine
        analyzed_protein = ProteinAnalysis(str(protein_sequence))
        
        # 1. Calculate Molecular Weight
        mw = analyzed_protein.molecular_weight()
        print(f"Molecular Weight: {mw:.2f} Da (Daltons)")
        
        # 2. Calculate Isoelectric Point (pI)
        pI = analyzed_protein.isoelectric_point()
        print(f"Isoelectric Point (pI): {pI:.2f}")

if __name__ == "__main__":
    fetch_and_read_protein()