## Jupyter Notebook on server

Follow the following steps to use Jupyter Notebook launched from remote server.

1. Launch Jupyter Notebook from remote server, selecting a port number for <PORT>:

```bash
jupyter notebook --no-browser --port=1303
```

**Please note the port setting**. You will need it in the next step.

2. You can access the notebook from your remote machine over SSH by setting up a SSH tunnel. Run the following command from your local machine:

```bash
ssh -L 8080:localhost:1303 adarsh@clear-antares.d2.comp.nus.edu.sg
```

The above command opens up a new SSH session in the terminal.

3. Open a browser from your local machine and navigate to `http://localhost:8080/`, the Jupyter Notebook web interface. Replace 8080 with your port number used in step 1.

```bash
jupyter notebook --no-browser --ip=2405:201:600a:c0b9:dff7:f139:bd4:5e39 --port=8888 
```

## ZSHRC aliases

```bash
alias shortlog='git log --graph --oneline --decorate --all -n'
alias anc='git add -A && git commit -am'
alias amend='git add -A && git commit --amend --no-edit'
alias out='deactivate'

function in {
    source ~/.venvs/"${1:-default}"/bin/activate
}

function listenvs {
    ls ~/.venvs/
}

function showhist {
    sqlite3 ~/Library/Safari/History.db \
    'SELECT
        datetime(V.visit_time+978307200, "unixepoch", "localtime") AS Time,
        substr(V.title, 1, 50) AS Title,
        substr(replace(replace(I.url, "https://", ""), "www.", ""), 1, 70) AS URL
 FROM history_visits V
 LEFT JOIN history_items I on V.history_item = I.id
 ORDER BY visit_time DESC
 LIMIT 4000;' -header -csv | subl
}
```