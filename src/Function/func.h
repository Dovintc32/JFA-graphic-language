#ifndef FUNC_H
#define FUNC_H

#include <string>
#include <json.hpp>

using json = nlohmann::json;

json load_json(const std::string& filename);
void save_json(const json& data, const std::string& filename);

#endif