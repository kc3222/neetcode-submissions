class Solution:
    def simplifyPath(self, path: str) -> str:
        # Split by "/"
        # Go through the split
        paths = path.split("/")
        res = []
        for i in range(len(paths)):
            folder = paths[i]
            if folder == "":
                continue
            elif folder == ".":
                continue
            elif folder == "..":
                if len(res) > 0:
                    res.pop()
            else:
                res.append(folder)
        return "/" + "/".join(res)