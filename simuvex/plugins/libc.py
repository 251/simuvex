from .plugin import SimStatePlugin

global heap_location
heap_location = 0xc0000000

class SimStateLibc(SimStatePlugin):
    """
    This state plugin keeps track of various libc stuff:
    """

    #__slots__ = [ 'heap_location', 'max_str_symbolic_bytes' ]

    LOCALE_ARRAY = [ 0x02, 0x00, 0x02, 0x00, 0x02, 0x00, 0x02, 0x00,
                    0x02, 0x00, 0x02, 0x00, 0x02, 0x00, 0x02, 0x00,
                    0x02, 0x00, 0x03, 0x20, 0x02, 0x20, 0x02, 0x20,
                    0x02, 0x20, 0x02, 0x20, 0x02, 0x00, 0x02, 0x00,
                    0x02, 0x00, 0x02, 0x00, 0x02, 0x00, 0x02, 0x00,
                    0x02, 0x00, 0x02, 0x00, 0x02, 0x00, 0x02, 0x00,
                    0x02, 0x00, 0x02, 0x00, 0x02, 0x00, 0x02, 0x00,
                    0x02, 0x00, 0x02, 0x00, 0x02, 0x00, 0x02, 0x00,
                    0x01, 0x60, 0x04, 0xc0, 0x04, 0xc0, 0x04, 0xc0,
                    0x04, 0xc0, 0x04, 0xc0, 0x04, 0xc0, 0x04, 0xc0,
                    0x04, 0xc0, 0x04, 0xc0, 0x04, 0xc0, 0x04, 0xc0,
                    0x04, 0xc0, 0x04, 0xc0, 0x04, 0xc0, 0x04, 0xc0,
                    0x08, 0xd8, 0x08, 0xd8, 0x08, 0xd8, 0x08, 0xd8,
                    0x08, 0xd8, 0x08, 0xd8, 0x08, 0xd8, 0x08, 0xd8,
                    0x08, 0xd8, 0x08, 0xd8, 0x04, 0xc0, 0x04, 0xc0,
                    0x04, 0xc0, 0x04, 0xc0, 0x04, 0xc0, 0x04, 0xc0,
                    0x04, 0xc0, 0x08, 0xd5, 0x08, 0xd5, 0x08, 0xd5,
                    0x08, 0xd5, 0x08, 0xd5, 0x08, 0xd5, 0x08, 0xc5,
                    0x08, 0xc5, 0x08, 0xc5, 0x08, 0xc5, 0x08, 0xc5,
                    0x08, 0xc5, 0x08, 0xc5, 0x08, 0xc5, 0x08, 0xc5,
                    0x08, 0xc5, 0x08, 0xc5, 0x08, 0xc5, 0x08, 0xc5,
                    0x08, 0xc5, 0x08, 0xc5, 0x08, 0xc5, 0x08, 0xc5,
                    0x08, 0xc5, 0x08, 0xc5, 0x08, 0xc5, 0x04, 0xc0,
                    0x04, 0xc0, 0x04, 0xc0, 0x04, 0xc0, 0x04, 0xc0,
                    0x04, 0xc0, 0x08, 0xd6, 0x08, 0xd6, 0x08, 0xd6,
                    0x08, 0xd6, 0x08, 0xd6, 0x08, 0xd6, 0x08, 0xc6,
                    0x08, 0xc6, 0x08, 0xc6, 0x08, 0xc6, 0x08, 0xc6,
                    0x08, 0xc6, 0x08, 0xc6, 0x08, 0xc6, 0x08, 0xc6,
                    0x08, 0xc6, 0x08, 0xc6, 0x08, 0xc6, 0x08, 0xc6,
                    0x08, 0xc6, 0x08, 0xc6, 0x08, 0xc6, 0x08, 0xc6,
                    0x08, 0xc6, 0x08, 0xc6, 0x08, 0xc6, 0x04, 0xc0,
                    0x04, 0xc0, 0x04, 0xc0, 0x04, 0xc0, 0x02, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
                  ]

    def __init__(self):
        SimStatePlugin.__init__(self)

        # various thresholds
        self.heap_location = heap_location
        self.buf_symbolic_bytes = 60
        self.max_symbolic_strstr = 1
        self.max_symbolic_strchr = 16
        self.max_variable_size = 128
        self.max_str_len = 128
        self.max_buffer_size = 48
        self.max_strtol_len = 10
        self.max_memcpy_size = 4096

        # strtok
        self.strtok_heap = [ ]
        self.simple_strtok = True
        self.strtok_token_size = 1024

        # helpful stuff
        self.strdup_stack = [ ]

        # as per Andrew:
        # the idea is that there's two abi versions, and for one of them, the
        # address passed to libc_start_main isn't actually the address of the
        # function, but the address of a pointer to a struct containing the
        # actual function address and the table of contents address
        self.ppc64_abiv = None

        # It will be initialized in __libc_start_main SimProcedure
        self.ctype_table_ptr = None

    def copy(self):
        c = SimStateLibc()
        c.heap_location = self.heap_location
        c.buf_symbolic_bytes = self.buf_symbolic_bytes
        c.max_symbolic_strstr = self.max_symbolic_strstr
        c.max_symbolic_strchr = self.max_symbolic_strchr
        c.max_variable_size = self.max_variable_size
        c.max_str_len = self.max_str_len
        c.max_buffer_size = self.max_buffer_size
        c.max_strtol_len = self.max_strtol_len
        c.max_memcpy_size = self.max_memcpy_size
        c.strtok_heap = self.strtok_heap[:]
        c.simple_strtok = self.simple_strtok
        c.strtok_token_size = self.strtok_token_size
        c.strdup_stack = self.strdup_stack[:]
        c.ppc64_abiv = self.ppc64_abiv
        c.ctype_table_ptr = self.ctype_table_ptr
        #c.aa = self.aa

        return c

    def merge(self, others, merge_flag, flag_values):
        merging_occured = False

        new_heap_location = max(o.heap_location for o in others)
        if self.heap_location != new_heap_location:
            self.heap_location = new_heap_location
            merging_occured = True

        return merging_occured, [ ]

    def widen(self, others, merge_flag, flag_values):

        # TODO: Recheck this function
        return self.merge(others, merge_flag, flag_values)

SimStatePlugin.register_default('libc', SimStateLibc)
