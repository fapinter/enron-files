import os

def readFiles(main_directory, graph):
    absolute_path = main_directory
    layer1_path = os.listdir(absolute_path)

    for i in layer1_path:
        layer2_path = os.listdir(f"{absolute_path}/{i}")
        
        for j in layer2_path:
            layer3_path = os.listdir(f"{absolute_path}/{i}/{j}")

            for k in layer3_path:
                file_path = absolute_path+"/"+i+"/"+j+"/"+k
                searching = True
                isolated = False

                #Some folders are still found in this directory layer
                #The try except structure avoids code breaking in this situations
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        sender = lines[2].strip()
                        sender = sender.lstrip("From: ")

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
                #Treatment for folders found on this directory layer
                except(IsADirectoryError) as e:
                    layer4_path = os.listdir(file_path)

                    for w in layer4_path:
                        new_file_path = file_path + "/"+ w

                        with open(new_file_path, 'r', encoding='utf-8') as f:
                            lines = f.readlines()
                            sender = lines[2].strip()
                            sender = sender.lstrip("From: ")

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