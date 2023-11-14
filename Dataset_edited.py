import os
import numpy as np
import torch
from torch_geometric.data import Dataset


class IG_Dataset(Dataset):
    def __init__(self, root, embedding=False, edge_features=False):
        super().__init__(root)

        self.data_dir = root
        self.embedding = embedding

        self.filepaths = [os.path.join(self.data_dir, file) for file in os.listdir(self.data_dir)]
        #self.input_data = {ind:torch.load(filepath) for ind, filepath in enumerate(self.filepaths)}
        
        self.input_data = {}
        
        # Process the input graphs
        ind = 0
        for file in self.filepaths:
            
            grph = torch.load(file)

            # Transform labels to negative log space and min-max scale
            lowest = 0
            highest = 16
            pK = -torch.log10(grph.affinity)
            pK_scaled = (pK - lowest) / (highest - lowest)
            grph.y = pK_scaled
            
            if self.embedding:
                grph.x = torch.cat((grph.x_lig, grph.x_prot_emb), axis=0)
            else:
                grph.x = torch.cat((grph.x_lig, grph.x_prot_aa), axis=0)

            if not edge_features:
                grph.edge_attr = grph.edge_attr[:,3].view(-1,1)
                grph.edge_attr_lig = grph.edge_attr_lig[:,3].view(-1,1)
                grph.edge_attr_prot = grph.edge_attr_prot[:,3].view(-1,1)

            grph.n_nodes = grph.x.shape[0]

            grph.data = grph.data.reshape(1, 3)

            # Introduce a master node for the protein nodes
            eim = grph.edge_index_master
            source = [i for i in range( max(eim[0])+1, max(eim[1]) )]
            dest = [max(eim[1]).item() for i in range(len(source))]
            grph.edge_index_master_prot = torch.tensor([source, dest], dtype=torch.int64)

            self.input_data[ind] = grph
            ind += 1


    def len(self):
        return len(self.input_data)
    
    def get(self, idx):
        graph = self.input_data[idx]
        return graph