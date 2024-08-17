class Solution:
    def simplifyPath(self, path: str) -> str:
        path_arr = path.split('/')
        new_path = []
        for folder in path_arr:
            if folder == ".." and len(new_path) > 0:
                new_path.pop(-1)
            elif folder != "." and folder != "" and folder != "..":
                new_path.append(folder)
        return "/" + "/".join(new_path)