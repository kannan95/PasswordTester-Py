import threading
import time
import string


characters = list(string.ascii_lowercase)
start_time = time.clock()


class password_brute_class(threading.Thread):

    def __init__(self, value, user_passwd):
        self.value = value
        self.user_passwd = user_passwd
        self.count = 0
        threading.Thread.__init__(self)

    def indexing(self, char, index_value):
        self.next_index = characters.index(char[index_value]) + 1
        if self.next_index <= len(characters) - 1:
            char[index_value] = characters[self.next_index]
        else:
            char[index_value] = characters[0]
            self.indexing(char, index_value - 1)

    def run(self,):
        self.start = list(characters[0] * (self.value + 1))
        self.end = list(characters[-1] * (self.value + 1))
        while self.start != self.end and self.start != self.user_passwd:
            self.count += 1
            self.indexing(self.start, self.value)
        if self.start == self.user_passwd:
            end_time = time.clock()
            global time_taken
            time_taken = end_time - start_time
            global guess_count
            guess_count = self.count
            # return time_taken
            # print("the password took {:5f} to bruteforce".format(end_time-start_clock))
            # print("It took {0} guesses".format(self.count))


def main(length, user_passwd):
    for i in range(length):
        password_brute_class(i, user_passwd).start()
    
    return time_taken, guess_count

    while True:
        pass



