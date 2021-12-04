BOARD_ROWS = 5
BOARD_COLS = 5

def parse_board(raw_board):
  rows = raw_board.split('\n')
  return [ [ int(r) for r in row.split(' ') if r != '' ] for row in rows]

def get_position_map(board):
  position = {}
  for r in range(BOARD_ROWS):
    for c in range(BOARD_COLS):
      entry = board[r][c]
      if entry in position:
        raise Exception("duplicate entry found in board")
      position[entry] = (r, c)
  return position

def check_row(board, marked_set, row_idx):
  return BOARD_COLS == len([ entry for entry in board[row_idx] if entry in marked_set])
    
def check_col(board, marked_set, col_idx):
  transposed_board = list(map(list, zip(*board)))
  return BOARD_ROWS == len([ entry for entry in transposed_board[col_idx] if entry in marked_set])

def play_bingo(sequence, boards, position_maps):
  marked_set = set()
  latest_result = None
  already_won = set()
  for num in sequence:
    marked_set.add(num)
    for board_idx in range(len(boards)):
      board = boards[board_idx]
      position_map = position_maps[board_idx]
      if num in position_map:
        row_idx, col_idx = position_map[num]
        if board_idx not in already_won and (check_row(board, marked_set, row_idx) or check_col(board, marked_set, col_idx)):
          already_won.add(board_idx)
          latest_result = (board, num, set(marked_set))
  return latest_result

def calculate_final_score(board, winning_number, marked_numbers):
  total = 0
  for row in board:
    for entry in row:
      if entry not in marked_numbers:
        total += entry
  return total * winning_number

f = open("input.txt", "r")
# f = open("small_input.txt", "r")

text = f.read()
sections = text.split("\n\n")
raw_sequence, *raw_boards = sections
sequence =  [ int(n) for n in raw_sequence.split(",") ]
boards = [ parse_board(raw_board) for raw_board in raw_boards ]
position_maps = [ get_position_map(board) for board in boards ]
board, winning_number, marked_numbers = play_bingo(sequence, boards, position_maps)
answer = calculate_final_score(board, winning_number, marked_numbers)
print(answer)