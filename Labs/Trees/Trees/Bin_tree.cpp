#include "Bin_tree.h"

Bin_tree::Bin_tree() {
	head = NULL;
    node = NULL;
    otr = false;
}
Tree_node* Bin_tree::find_bfs(Tree_node* tn) {
    q.push(tn);
    while (!q.is_empty()) {
        node = q.get();
        q.pop();
        if (node->left != NULL) {
            q.push(node->left);
        }
    else {
        node->left = new Tree_node;
        return node->left;
    }
    if (node->right != NULL) {
        q.push(node->right);
    }
    else {
        node->right = new Tree_node;
        return node->right;
    }
    }
    return node;
}

void Bin_tree::add_node(int a) {
    if (head == NULL) {
        head = new Tree_node;
        head->dat = a;
        return;
    }
    
    node = find_bfs(head);
    node->dat = a;
}

void Bin_tree::print(Tree_node* tn) {
    if (tn == NULL) {
        return;
    }
    cout << tn->dat << " ";
    print(tn->left);
    print(tn->right);
}

void Bin_tree::print_good(Tree_node* tn, int n) {
    long i;
    if (tn != NULL)
    {
        print_good(tn->right, n + 5);
        for (i = 0; i < n; i++)
            cout << " ";
        cout << tn->dat << endl;
        print_good(tn->left, n + 5);
    }
}

bool Bin_tree::check_parce(string &st) {
    Stek stek;
    for (int i = 0; i < st.length(); i++) {
        if (st[i] != ' ' and st[i] != ')' and st[i] != '(' and st[i] != '-' and (st[i] < '0' or st[i] > '9')) {
            cout << "Неверный символ: " << st[i] << endl;
            return false;
        }
        if (st[i] == '(') {
            stek.push('(');
        }
        else {
            if (st[i] == ')') {
                if (stek.get() == '(') {
                    stek.pop();
                }
                else {
                    cout << "Неверно выставлены скобки!\n";
                    return false;
                }
            }
        }
    }
    if (stek.get() != NULL) {
        cout << "Неверно выставлены скобки!\n";
        return false;
    }
    st[0] = ' ';
    for (int i = st.length() - 1; i > 0; i--) {
        if (st[i] == ')') {
            st[i] = ' ';
            break;
        }
        st[i] = ' ';
    }
    return true;
}
void Bin_tree::parce(Tree_node* tn, string st, int n) {
    if (head == NULL) {
        head = new Tree_node;
        tn = head;
    }
    int a = 0;
    if (st[n] == '-') {
        otr = true;
        parce(tn, st, n + 1);
    }

    if (st[n] >= '0' and st[n] <= '9') {
        while (st[n] >= '0' and st[n] <= '9') {
            a = a * 10 + st[n] - '0';
            n++;
        }
        if (otr) {
            a *= -1;
            otr = false;
        }
        tn->dat = a;
    }
   
    if (st[n] == ' ') {
      
        parce(tn, st, n + 1);
    }
    else
        if (tn->dat != 64) {
            if (st[n] == '(') {
                if (tn->left == NULL) {
                  
                    tn->left = new Tree_node;
                    tn->left->parent = tn;
                    parce(tn->left, st, n + 1);
                }
                else {
                    if (tn->right == NULL) {
                      
                        tn->right = new Tree_node;
                        tn->right->parent = tn;
                        parce(tn->right, st, n + 1);
                    }
                }
            }
            else {
                if (st[n] == ')') {
                    parce(tn->parent, st, n + 1);
                }
            }
        }
        else {
           
            parce(tn, st, n + 1);
        }
}

Tree_node* Bin_tree::get_head() {
    return head;
}

