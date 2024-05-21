export default function divideFunction(numerator, denominator) {
  if (denominator === 0 || Number.isNaN(denominator)) throw new Error('cannot divide by 0');
  return numerator / denominator;
}
