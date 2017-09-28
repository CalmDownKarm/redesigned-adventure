#include <iostream>
#include <vector>
#include <stack>
using namespace std;

/*Since the graph in this case is a Binary Tree, we'll use the array implementation of a tree
Every left child of a node contains the 2k successor and Right child contains 2k+1 successor
*/

int generate_left_child(int node){
    /*Take root and return the left child*/
    return 2*node;
}

int generate_right_child(int node){
    /*Take root and return the left child*/
    return (2*node)+1;
}

void print_stack(stack<int>mystack){
    stack<int> backup = mystack;
    cout<<endl;
    while(!backup.empty()){
        cout<<" "<<backup.top();
        backup.pop();
    }
}

void dfs(int goal_node, int start_node, int max_nodes){
    /*Runs DFS */
    //Check Starting Node
    if (start_node<=0 || goal_node<=0){
        cout<<"\n Illegal start or goal";
        return;
    }
    if (start_node ==  goal_node){
        cout<<"\n"<<start_node;
        return;
    }
    else{
        int nodes_generated = 1;
        int flag = 1;
        stack<int> mystack;
        vector<int> visited;
        //push start node onto stack
        mystack.push(start_node);
        cout<<"\n mystack "<<mystack.top();
        // visited.push_back(start_node);
        //Start popping a node, 
        //Check each popped node for goal state
        while(!mystack.empty()){
            int node_val = mystack.top();
            cout<<"\n Node Val "<<node_val;
            visited.push_back(node_val);
            if(goal_node == node_val){
                flag = 1;
                break;
                //disha@whitepanda.in
            }
            if(max_nodes < nodes_generated){
                //I've hit a leaf so pop 1 extra level
                print_stack(mystack);
                mystack.pop();
            }
            mystack.pop();
            mystack.push(generate_left_child(mystack.top()));
            mystack.push(generate_right_child(mystack.top()));
            nodes_generated*=2;
            
        }
        print_stack(mystack);
        if(flag){
            vector<int>::iterator itr;
            cout<<endl;
            for(itr = visited.begin();itr<visited.end();itr++)
                cout<<" "<<*itr;
        }
        else
            cout<<"\n Path Not Found";
        
        return;
    }
}

int main(){
    dfs(10,1,15);
}