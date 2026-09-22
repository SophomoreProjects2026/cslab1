// written by Noah
import {exec} from "child_process"

const Status = {
    ERROR: Symbol(),
    PASS: Symbol(),
    FAIL: Symbol(),
}

const tests = [
    {
        name: "Command Runs",
        command: "lgrep",
        evaluate: (output)=>{

        }
    }
]

const output = []

for (let i = 0; i < tests.length; i++) {
    const t = tests[i]
    exec(t.command, (err, stdout, stderr)=>{
        if (err) {
            console.log(`🟪 ${t.name}`);
            output[i] = {
                status: Status.ERROR,
                error: err,
            }
        } else if (t.evaluate(stdout)) {
            console.log(`🟩 ${t.name}`);
            output[i] = {
                status: Status.PASS,
            }
        } else {
            console.log(`🟥 ${t.name}`);
            output[i] = {
                status: Status.FAIL,
                output: stdout
            }
        }
    })
}