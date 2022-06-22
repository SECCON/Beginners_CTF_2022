#include <windows.h>

DWORD TLS = 0;
HANDLE hFlag;

DWORD check(char *flag) {
  LPVOID ans = TlsGetValue(TLS);

  if (strncmp(ans, flag, 0x100) == 0) {
    return 0;
  } else {
    return 1;
  }
}

DWORD WINAPI t1(LPVOID pflag) {
  char flag[0x100] = {};
  int j = 0;

  TlsSetValue(TLS, TEXT("c4{fAPu8#FHh2+0cyo8$SWJH3a8X"));

  for (int i = 0; i < sizeof(flag) / sizeof(char); i++) {
    char c = *(unsigned char*)(pflag + i);
    if (c == 0) break;
    if ((i % 3 == 0) || (i % 5 == 0))
      flag[j++] = c;
  }
  flag[j] = 0;

  return check(flag);
}

DWORD WINAPI t2(LPVOID pflag) {
  char flag[0x100];
  int j = 0;

  TlsSetValue(TLS, TEXT("tfb%s$T9NvFyroLh@89a9yoC3rPy&3b}"));

  for (int i = 0; i < sizeof(flag) / sizeof(char); i++) {
    char c = *(unsigned char*)(pflag + i);
    if (c == 0) break;
    if ((i % 3) && (i % 5))
      flag[j++] = c;
  }
  flag[j] = 0;

  return check(flag);
}

LRESULT CALLBACK WndProc(HWND hWnd , UINT msg , WPARAM wp , LPARAM lp) {
  switch (msg) {
  case WM_DESTROY:
    TlsFree(TLS);
    PostQuitMessage(0);
    return 0;

  case WM_CREATE:
    TLS = TlsAlloc();
    // textbox
    hFlag = CreateWindow(TEXT("EDIT"), TEXT(""),
                         WS_CHILD | WS_VISIBLE | WS_BORDER
                         | ES_AUTOHSCROLL |ES_LEFT,
                         16, 38, 200, 30, hWnd, (HMENU)0xdead,
                         ((LPCREATESTRUCT)(lp))->hInstance, NULL);
    // button
    CreateWindow(TEXT("BUTTON"), TEXT("check"),
                 WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON,
                 228, 38, 64, 30, hWnd, (HMENU)0x1337,
                 ((LPCREATESTRUCT)(lp))->hInstance, NULL);
    return 0;

  case WM_COMMAND: {
    DWORD dwID, retFizz, retBuzz;
    if (LOWORD(wp) != 0x1337) return 0;

    char flag[0x100];
    GetWindowText(hFlag, flag, 0x100);

    HANDLE thFizz = CreateThread(NULL, 0, t1, flag, 0, &dwID);
    HANDLE thBuzz = CreateThread(NULL, 0, t2, flag, 0, &dwID);
    WaitForSingleObject(thFizz, INFINITE);
    WaitForSingleObject(thBuzz, INFINITE);
    GetExitCodeThread(thFizz, &retFizz);
    GetExitCodeThread(thFizz, &retBuzz);
    CloseHandle(thFizz);
    CloseHandle(thBuzz);

    if (retFizz || retBuzz) {
      MessageBox(NULL, TEXT("Wrong flag..."), TEXT("NOPE"),
                 MB_OK | MB_ICONSTOP);
    } else {
      MessageBox(NULL, TEXT("Correct flag!"), TEXT("DOPE"),
                 MB_OK | MB_ICONINFORMATION);
    }
    return 0;
  }

  case WM_PAINT: { 
    HDC hdc;
    PAINTSTRUCT ps;
    hdc = BeginPaint(hWnd, &ps);
    TextOut(hdc, 8, 8, TEXT("Give me ticket:"), 15);
    EndPaint(hWnd, &ps);
    return 0;
  }
  }

  return DefWindowProc(hWnd , msg , wp , lp);
}

int WINAPI WinMain(HINSTANCE hInstance,
                   HINSTANCE hPrevInstance,
                   PSTR lpCmdLine,
                   int nCmdShow)
{
  HWND hWnd;
  MSG msg;
  WNDCLASS winc;

  winc.style         = CS_HREDRAW | CS_VREDRAW;
  winc.lpfnWndProc   = WndProc;
  winc.cbClsExtra    = winc.cbWndExtra = 0;
  winc.hInstance     = hInstance;
  winc.hIcon         = LoadIcon(NULL, IDI_APPLICATION);
  winc.hCursor       = LoadCursor(NULL, IDC_ARROW);
  winc.hbrBackground = GetStockObject(WHITE_BRUSH);
  winc.lpszMenuName  = NULL;
  winc.lpszClassName = TEXT("WinTLS");

  if (!RegisterClass(&winc))
    return 1;

  hWnd = CreateWindow(TEXT("WinTLS"),
                      TEXT("WinTLS - Beginners CTF 2022"),
                      WS_OVERLAPPED | WS_CAPTION | WS_SYSMENU | WS_VISIBLE,
                      CW_USEDEFAULT, CW_USEDEFAULT,
                      320, 128,
                      NULL, NULL, hInstance, NULL);
  if (hWnd == NULL)
    return 1;

  while (GetMessage(&msg, NULL, 0, 0)) {
    TranslateMessage(&msg);
    DispatchMessage(&msg);
  }

  return msg.wParam;
}
