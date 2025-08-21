#include "func.h"
#include <fstream>

json load_json(const std::string& filename) {
    std::ifstream file(filename);
    return json::parse(file);
}

void save_json(const json& data, const std::string& filename) {
    std::ofstream file(filename);
    file << data.dump(4);
}