def rps(p1, p2):
    if p1.lower() == 'scissors' and p2.lower() == 'paper':
        
        return "Player 1 won!"
    
    if p1.lower() == 'rock' and p2.lower() == 'scissors':
        
        return "Player 1 won!"
    
    if p1.lower() == 'paper' and p2.lower() == 'rock':
        
        return "Player 1 won!"
    
    if p1.lower() == 'scissors' and p2.lower() == 'rock':
        
        return "Player 2 won!"
    
    if p1.lower() == 'rock' and p2.lower() == 'paper':
        
        return "Player 2 won!"
    
    if p1.lower() == 'paper' and p2.lower() == 'scissors':
        
        return "Player 2 won!"

    if p1.lower() == p2.lower():

        return "Draw!"

    