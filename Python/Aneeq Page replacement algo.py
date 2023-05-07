import random

def FIFO(pages, pagefault, frame_size, page_frame):
    for page in pages:
        page_found = False
        
        for i in range(len(page_frame)):
            if(page_frame[i] == page):
                page_found = True
                break
            
        if not page_found and pagefault < frame_size:
            index = pagefault % frame_size
            page_frame.append(page)
            pagefault += 1
            print(page_frame, "\n")
            
        elif not page_found and pagefault >= frame_size:
            index = pagefault % frame_size
            page_frame[index] = page
            pagefault += 1
            print(page_frame, "\n")
        
        
    print("Page Faults occured: " , pagefault, "\n\n")
    return

def Optimal(pages, pagefault, frame_size, page_frame):
    index = 0
    for page in pages:
        page_found = False
        
        for i in range(len(page_frame)):
            if(page_frame[i] == page):
                page_found = True
                break
        
        if not page_found and pagefault < frame_size:
            index = pagefault % frame_size
            page_frame.append(page)
            pagefault += 1
        elif not page_found and pagefault >= frame_size:
            count = 0
            framefound = [-1] * len(page_frame)
            for j in range(index+1, len(pages)):
                for l in range(len(page_frame)):
                    if(pages[j] == page_frame[l] and framefound[l] == -1):
                        framefound[l] = count
                count += 1
            min_index = framefound.index(min(framefound))
            if(framefound[min_index] == -1):
                page_frame[min_index] = page
            else:
                max_index = framefound.index(max(framefound))
                page_frame[max_index] = page
            pagefault += 1
    
        print(page_frame , "\n")
        index += 1
    
    print("Page Faults occurred: " , pagefault)
    return

def LRU(pages, pagefault, frame_size, page_frame):
    index = 0
    for page in pages:
        page_found = False
        
        for i in range(len(page_frame)):
            if(page_frame[i] == page):
                page_found = True
                break
        
        if not page_found and pagefault < frame_size:
            index = pagefault % frame_size
            page_frame.append(page)
            pagefault += 1
        elif not page_found and pagefault >= frame_size:
            count = 0
            framefound = [0] * len(page_frame)
            for j in range(0,index):
                for l in range(len(page_frame)):
                    if(pages[j] == page_frame[l]):
                        framefound[l] = count
                count += 1
            min_index = framefound.index(min(framefound))
            page_frame[min_index] = page
            pagefault += 1
        print(page_frame , "\n")
        index += 1
    
    print("Page Faults occurred: " , pagefault)
    return

def Counting(pages, pagefault, frame_size, page_frame):
    PgCount = {}
    for page in pages:
        page_found = False
        
        if page not in PgCount:
            PgCount[page] = 0
        
        for i in range(len(page_frame)):
            if(page_frame[i] == page):
                page_found = True
                break
        
        if not page_found and pagefault < frame_size:
            index = pagefault % frame_size
            page_frame.append(page)
            pagefault += 1
        elif not page_found and pagefault >= frame_size:
            min_count = float('inf')
            replace_page = -1
            # finding the page in the page frame which has the least count
            for x in page_frame:
                if(min_count > PgCount[x]):
                    min_count = PgCount[x]
                    replace_page = x
            # looking for the page to be replaced in the page_frame
            for i in range(len(page_frame)):
                if(page_frame[i] == replace_page):
                    page_frame[i] = page
                    print("replaced page is: " , replace_page , "\n")
            # increasing the page fault
            pagefault += 1
        
        PgCount[page] += 1
        print(PgCount, "\n")
        print(page_frame , "\n")
    
    print("Page Faults occurred: " , pagefault)
    return

def SecondChance(pages, pagefault, frame_size, page_frame):
    # helps to track whether a process has been accessed or not
    accessed = [0] * frame_size
    index = 0
    for page in pages:
        page_found = False
        
        access = 0
        for i in range(len(page_frame)):
            accessed[i] = random.randint(0, 1)
            if(accessed[i] == 1):
                access += 1
                if(access == frame_size):
                    accessed[i] = 0
                    break
                print("page",page_frame[i]," was accessed\n")
        
        for i in range(len(page_frame)):
            if(page_frame[i] == page):
                page_found = True
                break
            
        if(not page_found and pagefault < frame_size):
            index = pagefault % frame_size
            page_frame.append(page)
            pagefault += 1
        elif(not page_found and pagefault >= frame_size):
            replace = False
            for j in range(len(page_frame)):
                if(accessed[j] == 1):
                    accessed[j] = 0
                elif(accessed[j] == 0 and replace == False):
                    print("page",page_frame[j]," is being replaced\n")
                    page_frame[j] = page
                    pagefault+=1
                    replace = True
        
        print(accessed , "\n")
        # print(page_frame, "\n")
        index += 1
        
    print("Page Faults occured: " , pagefault, "\n\n")
    return

pages = [7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,7,1]
pagefault = 0
# frame_size = int(input("Enter number of page frames: "))
frame_size = 3
page_frame = []
Counting(pages, pagefault, frame_size, page_frame)
# SecondChance(pages , pagefault , frame_size , page_frame) Test any function here no need to change the parameters
