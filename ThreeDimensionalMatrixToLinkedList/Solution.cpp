#include<bits/stdc++.h>
using namespace std;

class DirectionLinkedListNode {
public:
    int val;
    DirectionLinkedListNode *front;
    DirectionLinkedListNode *back;
    DirectionLinkedListNode *up;
    DirectionLinkedListNode *right;
    DirectionLinkedListNode *down;
    DirectionLinkedListNode *left;


    DirectionLinkedListNode(int x, DirectionLinkedListNode* f=NULL, DirectionLinkedListNode* b=NULL, DirectionLinkedListNode* u=NULL, DirectionLinkedListNode* r=NULL, DirectionLinkedListNode* d=NULL, DirectionLinkedListNode* l=NULL) {
        val = x;
        front = f;
        back = b;
        up = u;
        right = r;
        down = d;
        left = l;
    }
    vector<int> extractNeighbors()
    {
        vector<int > neighbour;
        // front back left right up down 
        neighbour.push_back(front->val);
        neighbour.push_back(back->val);
        neighbour.push_back(left->val);
        neighbour.push_back(right->val);
        neighbour.push_back(up->val);
        neighbour.push_back(down->val);
        return neighbour;
    }
};

class Solution{ 
    public:
        DirectionLinkedListNode* ThreeDimensionalMatrixToLinkedList(vector<vector<vector<int> > > a,int layer,int row,int column)
        {
        }  
};
