import torch
import torch.nn.functional as F
from torch_geometric.nn import global_mean_pool, GATv2Conv, global_add_pool, GCNConv


'''
# MODEL ARCHITECTURE SMALL BASELINE WITH GLOBAL MEAN POOL 
'''
class GAT0mp(torch.nn.Module):
    def __init__(self, dropout_prob, in_channels, edge_dim):
        super(GAT0mp, self).__init__()

        #Convolutional Layers
        self.conv1 = GATv2Conv(in_channels, 512, edge_dim=edge_dim)
        self.conv2 = GATv2Conv(512, 1024, edge_dim=edge_dim)
        self.conv3 = GATv2Conv(1024, 256, edge_dim=edge_dim)
        self.dropout_layer = torch.nn.Dropout(dropout_prob)
        self.fc1 = torch.nn.Linear(256, 64)
        self.fc2 = torch.nn.Linear(64, 1)

    def forward(self, graphbatch):
        
        x = self.conv1(graphbatch.x, graphbatch.edge_index, graphbatch.edge_attr)
        x = F.relu(x)
        x = self.conv2(x, graphbatch.edge_index, graphbatch.edge_attr)
        x = F.relu(x)
        x = self.conv3(x, graphbatch.edge_index, graphbatch.edge_attr)
        x = F.relu(x)

        # Pool the nodes of each interaction graph
        x = global_mean_pool(x, batch=graphbatch.batch)
        x = self.dropout_layer(x)

        # Fully-Connected Layers
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        return x


'''
# MODEL ARCHITECTURE SMALL WITH TWO ATTENTION HEADS (WITH AVERAGING) IN THE FIRST LAYER AND GLOBAL MEAN POOL 
'''
class GAT1mp(torch.nn.Module):
    def __init__(self, dropout_prob, in_channels, edge_dim):
        super(GAT1mp, self).__init__()

        #Convolutional Layers
        self.conv1 = GATv2Conv(in_channels, 512, edge_dim=edge_dim, heads=2, concat=False)
        self.conv2 = GATv2Conv(512, 1024, edge_dim=edge_dim)
        self.conv3 = GATv2Conv(1024, 256, edge_dim=edge_dim)
        self.dropout_layer = torch.nn.Dropout(dropout_prob)
        self.fc1 = torch.nn.Linear(256, 64)
        self.fc2 = torch.nn.Linear(64, 1)

    def forward(self, graphbatch):
        
        x = self.conv1(graphbatch.x, graphbatch.edge_index, graphbatch.edge_attr)
        x = F.relu(x)
        x = self.conv2(x, graphbatch.edge_index, graphbatch.edge_attr)
        x = F.relu(x)
        x = self.conv3(x, graphbatch.edge_index, graphbatch.edge_attr)
        x = F.relu(x)

        # Pool the nodes of each interaction graph
        x = global_mean_pool(x, batch=graphbatch.batch)
        x = self.dropout_layer(x)

        # Fully-Connected Layers
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        return x
    

'''
# MODEL ARCHITECTURE SMALL WITH TWO ATTENTION HEADS (WITH AVERAGING) IN THE FIRST TWO LAYERS AND GLOBAL MEAN POOL 
'''
class GAT2mp(torch.nn.Module):
    def __init__(self, dropout_prob, in_channels, edge_dim):
        super(GAT2mp, self).__init__()

        #Convolutional Layers
        self.conv1 = GATv2Conv(in_channels, 512, edge_dim=edge_dim, heads=2, concat=False)
        self.conv2 = GATv2Conv(512, 1024, edge_dim=edge_dim, heads=2, concat=False)
        self.conv3 = GATv2Conv(1024, 256, edge_dim=edge_dim)
        self.dropout_layer = torch.nn.Dropout(dropout_prob)
        self.fc1 = torch.nn.Linear(256, 64)
        self.fc2 = torch.nn.Linear(64, 1)

    def forward(self, graphbatch):
        
        x = self.conv1(graphbatch.x, graphbatch.edge_index, graphbatch.edge_attr)
        x = F.relu(x)
        x = self.conv2(x, graphbatch.edge_index, graphbatch.edge_attr)
        x = F.relu(x)
        x = self.conv3(x, graphbatch.edge_index, graphbatch.edge_attr)
        x = F.relu(x)

        # Pool the nodes of each interaction graph
        x = global_mean_pool(x, batch=graphbatch.batch)
        x = self.dropout_layer(x)

        # Fully-Connected Layers
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        return x




'''
# MODEL ARCHITECTURE SMALL WITH TWO ATTENTION HEADS (WITH AVERAGING) IN ALL THREE LAYERS AND GLOBAL MEAN POOL 
'''
class GAT3mp(torch.nn.Module):
    def __init__(self, dropout_prob, in_channels, edge_dim):
        super(GAT3mp, self).__init__()

        #Convolutional Layers
        self.conv1 = GATv2Conv(in_channels, 512, edge_dim=edge_dim, heads=2, concat=False)
        self.conv2 = GATv2Conv(512, 1024, edge_dim=edge_dim, heads=2, concat=False)
        self.conv3 = GATv2Conv(1024, 256, edge_dim=edge_dim, heads=2, concat=False)
        self.dropout_layer = torch.nn.Dropout(dropout_prob)
        self.fc1 = torch.nn.Linear(256, 64)
        self.fc2 = torch.nn.Linear(64, 1)

    def forward(self, graphbatch):
        
        x = self.conv1(graphbatch.x, graphbatch.edge_index, graphbatch.edge_attr)
        x = F.relu(x)
        x = self.conv2(x, graphbatch.edge_index, graphbatch.edge_attr)
        x = F.relu(x)
        x = self.conv3(x, graphbatch.edge_index, graphbatch.edge_attr)
        x = F.relu(x)

        # Pool the nodes of each interaction graph
        x = global_mean_pool(x, batch=graphbatch.batch)
        x = self.dropout_layer(x)

        # Fully-Connected Layers
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        return x



'''
# MODEL ARCHITECTURE SMALL WITH TWO ATTENTION HEADS (WITH CONCAT) IN THE FIRST LAYER AND GLOBAL MEAN POOL 
'''
class GAT1ccmp(torch.nn.Module):
    def __init__(self, dropout_prob, in_channels, edge_dim):
        super(GAT1ccmp, self).__init__()

        #Convolutional Layers
        self.conv1 = GATv2Conv(in_channels, 256, edge_dim=edge_dim, heads=2)
        self.conv2 = GATv2Conv(512, 1024, edge_dim=edge_dim)
        self.conv3 = GATv2Conv(1024, 256, edge_dim=edge_dim)
        self.dropout_layer = torch.nn.Dropout(dropout_prob)
        self.fc1 = torch.nn.Linear(256, 64)
        self.fc2 = torch.nn.Linear(64, 1)

    def forward(self, graphbatch):
        
        x = self.conv1(graphbatch.x, graphbatch.edge_index, graphbatch.edge_attr)
        x = F.relu(x)
        x = self.conv2(x, graphbatch.edge_index, graphbatch.edge_attr)
        x = F.relu(x)
        x = self.conv3(x, graphbatch.edge_index, graphbatch.edge_attr)
        x = F.relu(x)

        # Pool the nodes of each interaction graph
        x = global_mean_pool(x, batch=graphbatch.batch)
        x = self.dropout_layer(x)

        # Fully-Connected Layers
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        return x
    


'''
# MODEL ARCHITECTURE SMALL WITH TWO ATTENTION HEADS (WITH CONCAT) IN THE FIRST TWO LAYERS AND GLOBAL MEAN POOL 
'''
class GAT2ccmp(torch.nn.Module):
    def __init__(self, dropout_prob, in_channels, edge_dim):
        super(GAT2ccmp, self).__init__()

        #Convolutional Layers
        self.conv1 = GATv2Conv(in_channels, 256, edge_dim=edge_dim, heads=2)
        self.conv2 = GATv2Conv(512, 512, edge_dim=edge_dim, heads=2)
        self.conv3 = GATv2Conv(1024, 256, edge_dim=edge_dim)
        self.dropout_layer = torch.nn.Dropout(dropout_prob)
        self.fc1 = torch.nn.Linear(256, 64)
        self.fc2 = torch.nn.Linear(64, 1)

    def forward(self, graphbatch):
        
        x = self.conv1(graphbatch.x, graphbatch.edge_index, graphbatch.edge_attr)
        x = F.relu(x)
        x = self.conv2(x, graphbatch.edge_index, graphbatch.edge_attr)
        x = F.relu(x)
        x = self.conv3(x, graphbatch.edge_index, graphbatch.edge_attr)
        x = F.relu(x)

        # Pool the nodes of each interaction graph
        x = global_mean_pool(x, batch=graphbatch.batch)
        x = self.dropout_layer(x)

        # Fully-Connected Layers
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        return x
    




'''
# MODEL ARCHITECTURE SMALL WITH TWO ATTENTION HEADS (WITH CONCAT) IN ALL THREE LAYERS AND GLOBAL MEAN POOL 
'''
class GAT3ccmp(torch.nn.Module):
    def __init__(self, dropout_prob, in_channels, edge_dim):
        super(GAT3ccmp, self).__init__()

        #Convolutional Layers
        self.conv1 = GATv2Conv(in_channels, 256, edge_dim=edge_dim, heads=2)
        self.conv2 = GATv2Conv(512, 512, edge_dim=edge_dim, heads=2)
        self.conv3 = GATv2Conv(1024, 128, edge_dim=edge_dim, heads=2)
        self.dropout_layer = torch.nn.Dropout(dropout_prob)
        self.fc1 = torch.nn.Linear(256, 64)
        self.fc2 = torch.nn.Linear(64, 1)

    def forward(self, graphbatch):
        
        x = self.conv1(graphbatch.x, graphbatch.edge_index, graphbatch.edge_attr)
        x = F.relu(x)
        x = self.conv2(x, graphbatch.edge_index, graphbatch.edge_attr)
        x = F.relu(x)
        x = self.conv3(x, graphbatch.edge_index, graphbatch.edge_attr)
        x = F.relu(x)

        # Pool the nodes of each interaction graph
        x = global_mean_pool(x, batch=graphbatch.batch)
        x = self.dropout_layer(x)

        # Fully-Connected Layers
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        return x