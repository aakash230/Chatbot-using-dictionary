qna={
    'hi':'hello',
    'how r u': 'm fine',
    'i need some help':'sure tell me',
    'what are you doing?':'chatting with an interesting person.',
    'do you watch any movies':'yes i do',
    'fav movie':'The blind side,Intern and many more',
    'where are you from?':'Mumbai',
    'is it raining there?':'nope the sky is clear',
    'do you like sports':'yes i used to play football a lot'
    }

while (1):
    user_ques = input('You:  ').lower().strip()
    if user_ques in ['bye','ok bye','stop','done']:
        print('Bot: Bye')
        break
    elif user_ques not in qna.keys():
        print('Ask Something else')
    else:
        print('bot: ',qna[user_ques])
    
