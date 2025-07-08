import tempfile
import subprocess
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class RubyCode(BaseModel):
    code: str

@router.post("/ruby/exec")
def exec_ruby(request: RubyCode):
    try:
        with tempfile.NamedTemporaryFile(suffix=".rb", delete=False) as f:
            f.write(request.code.encode())
            f.flush()
            result = subprocess.run(["ruby", f.name], capture_output=True, text=True)
            return {"output": result.stdout or result.stderr}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
