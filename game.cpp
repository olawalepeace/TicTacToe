#include <iostream>
using namespace std;

char board[3][3] = {{' ',' ',' '},{' ',' ',' '},{' ',' ',' '}};
int turn = 1;

void DrawBoard();
void UpdateBoard(int row, int col, char player);
bool IsWin(char player);
bool IsEmpty(int row, int col);

int main(){
    char player ='O';
    int row_col[2];
    DrawBoard();
    for(;;){
        for(;;){//taking User input
            cout<<"Player "<<player<<", Input index of play";
            cin>>row_col[0]>>row_col[1];
            if(IsEmpty(row_col[0],row_col[1])){
                UpdateBoard(row_col[0], row_col[1], player);
                break;
            }else{
                cout<<"Error: Not Empty";
            }
        }
        
        if(IsWin(player)){
            cout<<"Player "<<player<<" wins";
            break;
        }else if(turn>9){
            cout<<"Game is a draw";
            break;
        }else{
            switch (player)
            {
            case 'X':
                player = 'O';
                break;
            
            case 'O':
                player = 'X';
                break;
            }
        }
    }
}

void DrawBoard(){
    for(int i=0;i<3;i++){
        cout<<"|";
        for (int j = 0; j < 3; j++){
            cout<<board[i][j]<<"|";
        }
        cout<<"\n";        
    }
}

bool IsEmpty(int row, int col){
    return (board[row][col] == ' ');
}

void UpdateBoard(int row, int col, char player){
    board[row][col] = player;
    DrawBoard();
    turn++;
}

bool IsWin(char player){
    if((board[0][0]==player && board[1][1]==player && board[2][2]==player) || (board[0][2]==player && board[1][1]==player && board[2][1]==player)){return true;}
    else{
        for(int i=0; i<3;i++){
            if((board[i][0]==player && board[i][1]==player && board[i][2]==player) || (board[0][i]==player && board[1][i]==player && board[2][i]==player)){
                return true;
                break;
            }
        }
    }
    return false;
}