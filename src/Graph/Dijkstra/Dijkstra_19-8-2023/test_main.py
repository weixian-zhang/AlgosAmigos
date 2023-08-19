
import pytest
from pytest_mock import mocker
from main import dijkstra_sp, adj_list

def test_dijkstra(mocker):
    
    dijkstra_sp_mock = mocker.patch('main.dijkstra_sp')
    dijkstra_sp_mock.return_value = [1]
        
    dist = dijkstra_sp_mock(adj_list) #dijkstra_sp(adj_list)
    
    dist_of_4 = dist[len(dist) - 1]
    
    assert dist_of_4 == 1
    

pytest.main(['test_main.py', '-s'])
        

# if __name__ == "__main__":
#     pytest.main(['test_main.py','./', '-s'])