def sex():
    import os
    import re
    for i in range(0, 9):
        f = open(str(i) + ".m3u", "r", encoding="utf8")
        original_list = []
        z = []
        list_name = []
        list_link = []
        list_group = []
        lines = f.readlines()
        for line in lines:
            line = line.rstrip("\r\n")
            if line.startswith("#EXTINF"):
                m = re.search("tvg-name=\"(.*?)\"", line)
                if m is not None:
                    list_name.append(m.group(1))
                else:
                    list_name.append(m)

                m = re.search("group-title=\"(.*?)\"", line)
                if m is not None:
                    list_group.append(m.group(1))
                else:
                    list_group.append(m)
            if line.startswith("http"):
                list_link.append(line)

        z = zip(list_name, list_link, list_group)
        original_list.append(list(z))
        final = []
        for i in range(len(original_list[0])):

            if original_list[0][i][0] is not None:
                if "SPORT" not in original_list[0][i][0]:
                    pass;
                else:
                    final.append(original_list[0][i])
        for i in range(len(original_list[0])):
            if original_list[0][i][0] is not None:
                if "sport" not in original_list[0][i][0]:
                    pass;
                else:
                    final.append(original_list[0][i])



        for i in range(len(final)):
            if final[i][2] in dic_group.keys():
                name = dic_group[final[i][2]]
                if final[i][0] in name.keys():
                    url = name[final[i][0]]
                    url.add(final[i][1])
                    name[final[i][0]] = url
                    dic_group[final[i][2]] = name

                else:
                    url = set()
                    url.add(final[i][1])
                    name[final[i][0]] = url
                    dic_group[final[i][2]] = name

            else:
                name = {}
                url = set()
                url.add(final[i][1])
                name[final[i][0]] = url
                dic_group[final[i][2]] = name

