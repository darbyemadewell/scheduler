import DailySchedule from "@/components/DailySchedule";

export default function Home() {
  return (
    <div className="m-10">
      <h1 className="text-4xl mb-4">Scheduler</h1>
      <DailySchedule />
    </div>
  );
}
