#include <iostream>
#include <string>
#include <vector>
#include <set>

using namespace std;

bool check(string& s, string& word, int head, int tail)
{
  int skip = (tail-head)/((int)word.size()-1);
  for(int i=head+skip, j=1; i!=tail; i+=skip,j++) {
    if(s[i]!=word[j]) return false;
  }
  return true;
}

int main(int argc, char** argv)
{
  string word = argv[1];
  string s;
  getline(cin, s);

  int len_word = (int)word.size();
  vector< vector<int> > mod_heads(len_word-1);
  vector< vector<int> > mod_tails(len_word-1);
  char head_char = word[0];
  char tail_char = word[len_word-1];
  for(int i=0;i<(int)s.size();i++) {
    if(s[i]==head_char)
      mod_heads[i%(len_word-1)].push_back(i);
    if(s[i]==tail_char)
      mod_tails[i%(len_word-1)].push_back(i);
  }

  set< pair<int, int> > ans;
  for(unsigned int i=0;i<mod_heads.size();i++) {
    for(unsigned int j=0;j<mod_heads[i].size();j++) {
      for(unsigned int k=0;k<mod_tails[i].size();k++) {
	int head = mod_heads[i][j];
	int tail = mod_tails[i][k];
	int skip = (tail-head)/(len_word-1);
	if(check(s, word, head, tail)) {
	  if(head<tail) ans.insert(make_pair(skip, head+1));
	  else ans.insert(make_pair(-skip, tail+1));
	}
      }
    }
  }

  for(set< pair<int,int> >::iterator it=ans.begin(); it!=ans.end(); ++it) {
    cout << it->first << "," << it->second << endl;
  }
  return 0;
}
