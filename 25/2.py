#Merry Christmas everyone :D!

#Advent of Code is over and I can go back to sleep

for day in range(1, 25 + 1):
    time = (1, 34)
    go_to_sleep()
    while time != (5, 45):
        time += sleep()
    wake_up_for_advent()
    boot_pc()
    open_advent_page()
    read_hacker_news()
    spam_click()

    for part in (1, 2):
        solved = False
        n_attempts = 0
        while not solved:
            try_new_solution()
            attempt()
            if n_attempts > 3:
                wait_cooldown()
            n_attempts += 1

    refactor_code()
    got_to_sleep()


"""
    _\/_
     /\
     /\
    /  \
    /~~\o
   /o   \
  /~~*~~~\
 o/    o \
 /~~~~~~~~\~`
/__*_______\
     ||
   \====/
    \__/
"""
