import pygame

def draw(enigma, path, screen, width, height, margins, gap, font):    

    
    # Width of individual components:
    w = (width - margins['left'] - margins['right'] - (5 * gap)) / 6 
    w += w/2/6
    h = height - margins['top'] - margins['bottom']

    # Draw path
    y = [margins['top']+(signal+1)*h/27 for signal in path]
    print(y)
    x = [width-margins['right'] - w/2]

    # Base coordinates
    x = margins['left']
    y = margins['top']

    # Draw enigma components
    for component in [enigma.U, enigma.L, enigma.M, enigma.R, enigma.P]:
        component.draw(screen, x, y, w, h, font)
        x += w + gap

    enigma.KB.draw(screen, x, y, w/2, h, font)
