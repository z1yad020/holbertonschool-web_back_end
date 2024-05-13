import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const res = [];
  res.push(new ClassRoom(19));
  res.push(new ClassRoom(20));
  res.push(new ClassRoom(34));
  return res;
}
