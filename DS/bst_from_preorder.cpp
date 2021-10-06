#include <bits/stdc++.h>
using namespace std;

struct Node{
    int val;
    Node *left;
    Node *right;
};

Node *getNewNode(int val){
    Node *newNode;
    newNode->val = val;
    newNode->left = newNode->right = NULL;
    return newNode;
}

int constructBst(vector<int> &preorder, int n, int pos, Node *current, int left, int right){
    
    if(pos==n || preorder[pos]<left || preorder[pos]>right)
            return pos;
        
    if(preorder[pos]<current->val)
    {
        current->left = getNewNode(preorder[pos]);
        pos += 1;
        pos = constructBst(preorder,n,pos,current->left,left,current->val-1);
    }
        
    if(pos==n || preorder[pos]<left || preorder[pos]>right)
        return pos;
        
    current->right = getNewNode(preorder[pos]);
    pos += 1;
    pos = constructBst(preorder,n,pos,current->right,current->val+1,right);
    return pos;
}

Node* bstFromPreorder(vector<int>& preorder) {    
    int n = preorder.size();
    if(n==0)
        return NULL;
        
    Node *root = getNewNode(preorder[0]);
    if(n==1)
        return root;

    constructBst(preorder,n,1,root,INT_MIN,INT_MAX);
    return root;
}
