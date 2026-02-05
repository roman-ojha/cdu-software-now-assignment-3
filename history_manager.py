class HistoryManager:
    """
    Class that handles the Undo & Redo logic using stacks.
    """

    def __init__(self):
        self._undo_stack = []
        self._redo_stack = []

    def push_state(self, image):
        """This method is used to push the current image state into undo stack and clear the redo stack."""
        if image is not None:
            self._undo_stack.append(image.copy())
            self._redo_stack.clear()

    def undo(self, current_image):
        """This method is used to pop the last image state from the undo stack and push the current image state into the redo stack and then return that popped image state to display it on the canvas."""
        if self._undo_stack:
            self._redo_stack.append(current_image)
            return self._undo_stack.pop()
        return None

    def redo(self, current_image):
        """This method is used to pop the last image state from the redo stack and push the current image state into the undo stack and then return that popped image state to display it on the canvas."""
        if self._redo_stack:
            self._undo_stack.append(current_image)
            return self._redo_stack.pop()
        return None
