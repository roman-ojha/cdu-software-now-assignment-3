class HistoryManager:
    """
    Class that handles the 'Undo' and 'Redo' logic using stacks.
    """

    def __init__(self):
        self._undo_stack = []
        self._redo_stack = []

    def push_state(self, image):
        """
        Saves the current image state to the undo stack.
        Clears the redo stack whenever a new action is performed.
        """
        if image is not None:
            self._undo_stack.append(image.copy())
            self._redo_stack.clear()

    def undo(self, current_image):
        """
        Restores the previous image state.
        Returns the previous image if available, else None.
        """
        if self._undo_stack:
            # Save current state to redo before undoing
            self._redo_stack.append(current_image)
            return self._undo_stack.pop()
        return None

    def redo(self, current_image):
        """
        Re-applies a previously undone state.
        Returns the redo image if available, else None.
        """
        if self._redo_stack:
            # Save current state to undo before redoing
            self._undo_stack.append(current_image)
            return self._redo_stack.pop()
        return None
        
