import os
from PDBbind_Dataset import IG_Dataset

# Dataset Construction
train_dir = 'PDBbind1'
dataset = 'train'
data_split = './PDBbind_data_splits/PDBbind_c0_data_split.json'
refined_only = False
exclude_ic50 = False
exclude_nmr = False
resolution_threshold = 5
precision_strict = False
delete_ligand = False
delete_protein = False

# Graph Construction
protein_embeddings = ['ankh', 'esm2_t6']
ligand_embeddings = ['ChemBERTa_10M']
masternode = True
masternode_connectivity = 'all'
masternode_edges='undirected'
atom_features = True
edge_features = True


dataset = IG_Dataset(   train_dir,
                        dataset=dataset,
                        data_split=data_split,
                        protein_embeddings=protein_embeddings,
                        ligand_embeddings=ligand_embeddings,
                        masternode=masternode,
                        masternode_connectivity=masternode_connectivity,
                        masternode_edges=masternode_edges,
                        edge_features=edge_features, 
                        atom_features=atom_features, 
                        refined_only=refined_only,
                        exclude_ic50=exclude_ic50,
                        exclude_nmr=exclude_nmr,
                        resolution_threshold=resolution_threshold,
                        precision_strict=precision_strict, 
                        delete_ligand=delete_ligand,
                        delete_protein=delete_protein)