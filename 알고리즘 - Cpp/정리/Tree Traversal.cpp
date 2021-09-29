#include <iostream>

using namespace std;

class Tree{
    string data;
    Tree* left, *right;
public:
    Tree(){
        data = "";
        left = NULL;
        right = NULL;
    }
    void setData(char data){ this->data = data; }
    void setLeft(Tree* left){ this->left = left; }
    void setRight(Tree* right){ this->right = right; }
    void static preorder(Tree* root){ // !!static을 넣어서 멤버 함수에 객체 없이 접근 가능.
        if(root){
            cout << root->data;
            preorder(root->left);
            preorder(root->right);
        }
    }
    void static inorder(Tree* root){
        if(root){
            inorder(root->left);
            cout << root->data;
            inorder(root->right);
        }
    }
    void static postorder(Tree* root){
        if(root){
            postorder(root->left);
            postorder(root->right);
            cout << root->data;
        }
    }
};

int main(void){
    int n; // 노드 개수.
    cin >> n;
    Tree* tree = new Tree[n];
    for(int i = 0; i < n; ++i){
        char data, left, right;
        cin >> data >> left >> right;
        if(data != '.'){
            tree[data-'A'].setData(data);
        }
        if(left != '.'){
            tree[data-'A'].setLeft(&tree[left-'A']);
        }
        if(right != '.'){
            tree[data-'A'].setRight(&tree[right-'A']);
        }
    }
    Tree::preorder(&tree[0]);
    cout << "\n";
    Tree::inorder(&tree[0]);
    cout << "\n";
    Tree::postorder(&tree[0]);

    return 0;
}
