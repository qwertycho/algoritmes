// linkedList.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

class Node {
public:
	int value;
	Node* left;
	Node* right;
	Node(int value) {
		this->value = value;
		this->left = NULL;
		this->right = NULL;
	}

	void insert(int value) {
		if (value < this->value) {
			if (this->left == NULL) {
				this->left = new Node(value);
			}
			else {
				this->left->insert(value);
			}
		}
		else {
			if (this->right == NULL) {
				this->right = new Node(value);
			}
			else {
				this->right->insert(value);
			}
		}
	}
};

void printTree(Node* root) {
	if (root == NULL) {
		return;
	}
	printTree(root->left);
	std::cout << root->value << std::endl;
	printTree(root->right);
}

int main()
{
	Node root(10);
	root.insert(5);
	root.insert(15);
	root.insert(8);
	root.insert(3);
	root.insert(20);

	printTree(&root);

}
