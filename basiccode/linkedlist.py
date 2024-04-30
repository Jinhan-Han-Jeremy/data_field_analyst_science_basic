class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.node_count = 0
        self.head = None
        self.tail = None
##노드 더하기
    def add(self, item):
        new_node = Node(item)
        if self.node_count == 0:
          #첨엔 머리 더하기
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        ##노드 갯수 더하기
        self.node_count += 1

##연결리스트 순회로 새로운 리스트 만들기
    def traverse(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result

## 해당 인덱스 위치의 값 찾기
    def get_at(self, position): # 1부터 시작
        ## 인덱스에 벗어나는 포지션 가려내기
        if position <= 0 or position > self.node_count:
           return None

        current_node = self.head
        for i in range(position - 1):
            ##루프 횟수마다 넥스트로 현재 노드값 업데이트
            current_node = current_node.next
        return current_node
  
    def get_length(self):
        return self.node_count
##원소 삽입
    def insert_at(self, pos, new_node):
        if pos < 1 or pos > self.node_count + 1:
            return False

        if pos == 1:
            new_node.next = self.head
            self.head = new_node

        else:
            if pos == self.node_count + 1:
                prev = self.tail
            else:
                prev = self.get_at(pos - 1)
            new_node.next = prev.next
            prev.next = new_node

        if pos == self.node_count + 1:
            self.tail = new_node

        self.node_count += 1
        return True
##원소 삭제
    def pop_at(self, pos):
            if pos < 1 or pos > self.node_count:
                raise IndexError

            prev_node = None
            if pos == 1:
                popped_node = self.head
                self.head = popped_node.next
            elif pos <= self.node_count:
                prev_node = self.get_at(pos - 1)
                popped_node = prev_node.next
                prev_node.next = popped_node.next

            if pos == self.node_count:
                self.tail = prev_node

            self.node_count -= 1
            return popped_node.data
##두리스트 합치기
    def concatenate(self, other_list):
        if self.tail:
            self.tail.next = other_list.head
            if other_list.tail:
                self.tail = other_list.tail
        else:
            self.head = other_list.head
            self.tail = other_list.tail
        self.node_count += other_list.node_count
        other_list.head = None
        other_list.tail = None
        other_list.node_count = 0
