from linkedlist import *

def main(argv):
    # 빈 연결 리스트 생성
    my_list = LinkedList()

    # 노드 추가
    my_list.add(4)
    my_list.add(2)
    my_list.add(3)
    my_list.add(1)

    # 연결 리스트 순회
    print("Linked list:", my_list.traverse())

    # 특정 위치의 노드 얻기
    position = 2
    node_at_position = my_list.get_at(position)
    if node_at_position:
        print("Node at position", position, ":", node_at_position.data)
    else:
        print("Node at position", position, "not found")

    # 연결 리스트의 길이 확인
    print("Length of the linked list:", my_list.get_length())

    # 새로운 노드 추가하여 삽입
    new_node = Node(4)
    insert_position = 2
    my_list.insert_at(insert_position, new_node)

    # 연결 리스트 순회
    print("Linked list after insertion:", my_list.traverse())

    # 특정 위치의 노드 삭제
    delete_position = 3
    deleted_node_data = my_list.pop_at(delete_position)
    print("Deleted node data at position", delete_position, ":", deleted_node_data)

    # 연결 리스트의 길이 확인
    print("Length of the linked list after deletion:", my_list.get_length())

    # 연결 리스트 순회
    print("Linked list after deletion:", my_list.traverse())

    # 두 연결 리스트 합치기
    other_list = LinkedList()
    other_list.add(5)
    other_list.add(6)
    other_list.add(7)

    my_list.concatenate(other_list)
    print("Linked list after concatenation:")

if __name__ == "__main__":
    import sys
    main(sys.argv)