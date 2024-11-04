#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <memory>
#include <array>

struct node_t {
    std::shared_ptr<node_t> left;
    std::shared_ptr<node_t> right;
    long val;
};

bool is_valid_bst(std::shared_ptr<node_t> root, 
        long l_bound = LONG_MIN, long u_bound = LONG_MAX) {
    if (!root) return true;
    if (root->val < l_bound || root->val > u_bound) return false;
    if (!is_valid_bst(root->left, l_bound, root->val)) return false;
    if (!is_valid_bst(root->right, root->val, u_bound)) return false;
    return true;
}

class rbt_validator_t {
    rbt_validator_t(std::shared_ptr<node_t> __root, int __max_height): 
        tree_root(__root), max_height(__max_height) {}
    bool is_valid_tree(void) {
        if (!is_valid_bst(this->tree_root)) return false;
        bool result = false;
        for (int i = 0; i <= this->max_height; i++) {
            result = result || this->validate_node(this->tree_root, i, 0);
            result = result || this->validate_node(this->tree_root, i, 1);
        }
        return result;
    }
    virtual ~rbt_validator_t() = default;
protected:
    bool validate_node(std::shared_ptr<node_t> root, int height, int color) {
        if (!root) return (height == 0);
        if (this->cache.find(root) != this->cache.end() && 
                this->cache[root].find(height) != this->cache[root].end() &&
                this->cache[root][height][color] != -1) {
            return static_cast<bool>(this->cache[root][height][color]);
        }
        if (this->cache[root].find(height) == this->cache[root].end()) {
            this->cache[root][height][0] = static_cast<short>(-1);
            this->cache[root][height][1] = static_cast<short>(-1);
        }
        bool result = false;
        if (color == 0) {
            result = this->validate_node(root->left, height - 1, 0);
            result = result || this->validate_node(root->left, height - 1, 1);
            result = result || this->validate_node(root->right, height - 1, 0);
            result = result || this->validate_node(root->right, height - 1, 1);
        } else {
            result = this->validate_node(root->left, height, 0);
            result = result || this->validate_node(root->right, height, 0);
        }
        this->cache[root][height][color] = static_cast<short>(result);
        return result;
    }
    std::map<std::shared_ptr<node_t>, std::map<int, std::array<short, 2>>> cache;
    std::shared_ptr<node_t> tree_root;
    int max_height = 0;
};
