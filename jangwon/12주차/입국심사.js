function solution(n, times) {
  let answer = Infinity;

  times.sort((a, b) => a-b);
  let left = 0;
  //가장 최대의 시간
  let right = times[times.length - 1] * n;

  // 가장 최소의 시간을 찾을 때까지 계속 탐색한다.
  while (left <= right) {
    let mid = parseInt((left + right) / 2);
    let cnt = 0;

    for (let i = 0; i < times.length; i++) {
      cnt += parseInt(mid / times[i]);
        // console.log(cnt);
      // if (cnt >= n) {
      //     console.log(cnt);
        answer = Math.min(answer, mid);
      // }
    }
  cnt >= n ? right = mid - 1 : left = mid + 1;
  }
  return answer;
};