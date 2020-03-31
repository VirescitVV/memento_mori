import os

#a dtg header that can be printed on any screen
def dtg_header(date, dow, time):
    print(f'\n        | {date} |    | {dow} |    | {time} UTC|\n')
    print('\n                       **Memento Mori**')

#a quote header that is ideal for the main screen only
def quote_header():
    print('\n“Let us prepare our minds as if we’d come to the very end of life.\n'
            '  Let us postpone nothing. Let us balance life’s books each day.\n'
            '  … The one who puts the finishing touches on their life each day\n'
            '              is never short of time.” — Seneca\n')
    print(' -----------------------------------------------------------------')
    print('\n“The recognition that I needed to train and discipline my character.\n'
            '  Not to be sidetracked by my interest in rhetoric. Not to write\n'
            '  treatises on abstract questions, or deliver moralizing little\n'
            ' sermons, or compose imaginary descriptions of The Simple Life or\n'
            '   The Man Who Lives Only for Others. To steer clear of oratory,\n'
            '  poetry and belles lettres. Not to dress up just to stroll around\n'
            '    the house, or things like that. To write straightforward.”\n'
            '                      — Marcus Aurelius\n')

#prints both the dtg header and the quote header after clearing the screen
def print_header_dtg(date, dow, time):
    os.system('clear')
    dtg_header(date, dow, time)
    quote_header()
