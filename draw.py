import pygame

def draw(enigma, path, screen, width, height, margins, gap, font):    

    
    # Width of individual components:
    w = (width - margins['left'] - margins['right'] - (5 * gap)) / 6 
    w += w/2/6
    h = height - margins['top'] - margins['bottom']

    # Path coordinates
    y = [margins['top']+(signal+1)*h/27 for signal in path]
    x = [width-margins['right'] - w/3] # Keyboard
    # Forward pass
    for i in [4,3,2,1,0]:
        x.append(margins['left'] + (i * gap) + (i * w) + w*3/4)
        x.append(margins['left'] + (i * gap) + (i * w) + w*1/4)
    # Backward pass
    for i in [0,1,2,3,4]:
        x.append(margins['left'] + (i * gap) + (i * w) + w*3/4)
        x.append(margins['left'] + (i+1) * gap + (i+1) * w + w*1/4)
    
    x.append(width-margins['right']-w/2) # Lampboard
    # Draw the path
    # print(len(path))
    # print(path)
    
    if len(path) > 0:
        for i in range(1, len(path)):
            start = (x[i-1], y[i-1])
            end = (x[i], y[i])
            if i < 10:
                c = 'teal'
            elif i in [10, 11]:
                c = 'gold'
            else:
                c = 'red'
            pygame.draw.line(screen, c, start, end, width=3)

    # Base coordinates
    x = margins['left']
    y = margins['top']

    # Draw enigma components
    for component in [enigma.U, enigma.L, enigma.M, enigma.R, enigma.P]:
        component.draw(screen, x, y, w, h, font)
        x += w + gap

    
    enigma.KB.draw(screen, x, y, w/2, h, font)

    # Add component names
    names = ['Reflector', 'Left', 'Middle', 'Right', 'Plugboard']
    for i in range(len(names)):
        x = margins['left'] + i * w + i * gap + w/2
        name = font.render(names[i], True, 'grey')
        text_box = name.get_rect(center = (x, margins['top']*.8))
        screen.blit(name, text_box)

