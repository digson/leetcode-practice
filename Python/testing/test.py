def remove_dups_no_buffer(head):
    current = head
    while current:
        # Runner starts at current and checks ahead
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                # Remove the duplicate
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next