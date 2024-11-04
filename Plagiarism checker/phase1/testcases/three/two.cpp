#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <memory>
#include <array>

struct Node {
    std::shared_ptr<Node> l;
    std::shared_ptr<Node> r;
    long long val;
};

bool isValidBST(std::shared_ptr<Node> root, 
        long long l_bound = LONG_MIN, long long u_bound = LONG_MAX) {
    if (!root) return true;
    if (root->val < l_bound || root->val > u_bound) return false;
    if (!isValidBST(root->l, l_bound, root->val)) return false;
    if (!isValidBST(root->r, root->val, u_bound)) return false;
    return true;
}

class RBTValidator {
    RBTValidator(std::shared_ptr<Node> __root, int __max_h): 
        tree_root(__root), max_h(__max_h) {}
    bool isValidTree(void) {
        if (!isValidBST(this->tree_root)) return false;
        for (int i = 0; i <= this->max_h; i++) {
            if (this->isRBTRoot(this->tree_root, i, 0) || 
                    this->isRBTRoot(this->tree_root, i, 1)) {
                return true;
            }
        }
        return false;
    }
    virtual ~RBTValidator() = default;
protected:
    bool isRBTRoot(std::shared_ptr<Node> root, int h, int c) {
        if (!root) return (h == 0);
        if (this->dp.find(root) != this->dp.end() && 
                this->dp[root].find(h) != this->dp[root].end() &&
                this->dp[root][h][c] != -1) {
            return this->dp[root][h][c];
        }
        if (this->dp[root].find(h) == this->dp[root].end()) {
            this->dp[root][h] = std::array<short, 2>({-1, -1});
        }
        bool rb = false;
        bool rr = false;
        if (c == 0) {
            rb = this->isRBTRoot(root->l, h - 1, 0);
            rb = rb || this->isRBTRoot(root->l, h - 1, 1);
            rb = rb || this->isRBTRoot(root->r, h - 1, 0);
            rb = rb || this->isRBTRoot(root->r, h - 1, 1);
        } else {
            rr = this->isRBTRoot(root->l, h, 0);
            rr = rr || this->isRBTRoot(root->r, h, 0);
        }
        this->dp[root][h][c] = rb || rr;
        return static_cast<bool>(this->dp[root][h][c]);
    }
    std::map<std::shared_ptr<Node>, std::map<int, std::array<short, 2>>> dp;
    std::shared_ptr<Node> tree_root;
    int max_h = 0;
};
