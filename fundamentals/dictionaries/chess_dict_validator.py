board1 = {'h1' : 'bking',
        #   'h2' : 'bking',
          'c6' : 'wqueen',
          'g2' : 'bbishop',
          'h5' : 'bqueen',
          'e3' : 'wking'

        #   'a1' : 'wking',
        #   'e4' : 'bpawn',
        #   'e6' : 'bpawn',
        #   'a2' : 'bpawn',
        #   'b2' : 'bpawn',
        #   'c2' : 'bpawn',
        #   'd2' : 'bpawn',
        #   'e2' : 'bpawn',
        #   'f2' : 'bpawn',
        #   'g2' : 'bpawn'
            # 'i13' : 'bqueen'
          }


def isValidChessBoard(board: dict)->bool:
    wcount = {}
    bcount = {}
    wtotal = 0
    btotal = 0

    if ('wking' or 'bking') not in board.values():
        return False

    for piece in board.values():

        if piece.startswith('w') == True:
            wcount.setdefault(piece, 0)
            wcount[piece] += 1
            wtotal += 1

        elif piece.startswith('b') == True:
            bcount.setdefault(piece, 0)
            bcount[piece] += 1
            btotal += 1

    print(bcount)
    print(wcount)

    try:
        if (wcount['wking'] > 1) or (bcount['bking'] > 1):
            return False
    except KeyError:
        return False
    
    if any(total > 16 for total in (wtotal,btotal)):
        return False

    try:
        if wcount['wpawn'] > 8:
            # any((int(total) > 8) for total in (wcount['wpawn'],bcount['bpawn'])):
            return False
    except KeyError:
        pass

    try:
        if bcount['bpawn'] > 8:
            return False
    except KeyError: # their are no pawns
        pass

    for key in board.keys():
        if len(key) > 2:
            return False
        if any(letter in key for letter in list('ijklmnopqrstuvwxyz')):
            return False
        if key.startswith(tuple('abcdefgh')) != True:
            return False
        if key.endswith(tuple('12345678')) != True:
            return False
    return True


if isValidChessBoard(board1) == False:
    print('Board invalid')
else:
    print('Board valid')