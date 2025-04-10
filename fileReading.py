import os

def readFiles(main_directory, graph):
    absolute_path = main_directory
    layer1_path = os.listdir(absolute_path)

    #Travels through the main directories until it reaches the files
    for i in layer1_path:
        layer2_path = os.listdir(f"{absolute_path}/{i}")
        
        for j in layer2_path:
            layer3_path = os.listdir(f"{absolute_path}/{i}/{j}")

            for k in layer3_path:
                file_path = absolute_path+"/"+i+"/"+j+"/"+k


                #Some folders are still found in this directory layer
                #The try except structure avoids code breaking in this situations
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        sender = lines[2].strip()
                        sender = sender.lstrip("From: ")


                        searching = True
                        isolated = False
                        line_it = 3
                        list_contacts = list()
                        #Performs a complete search of all emails that can be in the file
                        while searching:
                            curr_line = lines[line_it]

                            if curr_line.startswith("Subject:"):
                                searching = False
                                
                                #Email has no "To: " isolated nodes aren't added to the graph
                                if line_it == 3:
                                    isolated = True
                            else:
                                if curr_line.startswith("To: "):
                                    curr_line = curr_line.lstrip("To: ")
                                list_contacts.extend([email.strip() for email in curr_line.split(',') if email.strip()])
                                line_it += 1

                        if not isolated:
                            graph.add_node(sender)

                            for item in list_contacts:
                                graph.add_edge(sender, item)

                #Treatment for folders found on this directory layer
                #isADirectory and Permission Error are both the same Error,
                #but the first is the error generated on linux and second
                #is the error generated on Windows
                except(IsADirectoryError, PermissionError) as e:
                    layer4_path = os.listdir(file_path)

                    #Adds another listdir to make sure the entire folder is searched
                    for w in layer4_path:
                        new_file_path = file_path + "/"+ w

                        with open(new_file_path, 'r', encoding='utf-8') as f:
                            lines = f.readlines()
                            sender = lines[2].strip()
                            sender = sender.lstrip("From: ")

                            searching = True
                            isolated = False
                            line_it = 3
                            list_contacts = list()
                            #Performs a complete search of all emails that can be in the file
                            while searching:
                                curr_line = lines[line_it]

                                if curr_line.startswith("Subject:"):
                                    searching = False

                                    #Email not sent, just written, doesnt add to the graph
                                    if line_it == 3:
                                        isolated = True
                                else:
                                    if curr_line.startswith("To: "):
                                        curr_line = curr_line.lstrip("To: ")

                                    list_contacts.extend([email.strip() for email in curr_line.split(',') if email.strip()])
                                    line_it += 1
                            
                            if not isolated:
                                graph.add_node(sender)
                                for item in list_contacts:
                                    graph.add_edge(sender, item)


#After the graph is loaded, this function can be called to pass the structure to a .txt
def send_to_txt(graph):
    with open('graph_structure.txt', 'w', encoding="utf-8") as f:
        f.write("*** Adjacency List ***\n")

        for key in graph.adjacency_list.keys():
            f.write(f'{key}:\n')

            for id, value in graph.adjacency_list[key]:
                f.write(f'\t({id}, {value}) ->\n')
                
            f.write("\n")
        f.write("*"*22)